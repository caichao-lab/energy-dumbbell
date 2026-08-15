#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo/rag_ingest.py - RAG 知识库导入演示脚本（无依赖骨架版）

功能说明：
1. 自动扫描 dist/01_core（核心推理库）和 dist/02_cases（案例库）
2. 将每个 Markdown 文件按标题（## / ###）拆分成语义块（Chunks）
3. 输出统计报告（文件数、块数、总字符数）
4. 生成 chunks_sample.json 供人工检查分块效果

使用方法：
    python rag_ingest.py

输出示例：
    📁 正在扫描 01_core (../dist/01_core)
      ✅ 底层系统提示词（主文件）.md -> 12 个语义块
      ✅ R规则库.md -> 35 个语义块
      ...
    📊 总语义块数: 267
    📄 已生成示例文件: demo/chunks_sample.json
"""

import os
import sys
import glob
import re
import json
from pathlib import Path

# ==================== 配置区域 ====================
# 自动定位仓库根目录（假设 rag_ingest.py 在 demo/ 下）
BASE_DIR = Path(__file__).parent.parent.resolve()
CORE_DIR = BASE_DIR / "dist" / "01_core"
CASES_DIR = BASE_DIR / "dist" / "02_cases"

# 忽略的文件（不进入知识库）
IGNORE_FILES = {"README.md", "INDEX.md", "Term_Glossary.md"}

# 分块最小字符数（低于此值的块将被过滤）
MIN_CHUNK_SIZE = 20
# =================================================


def load_and_chunk(directory, source_name):
    """
    扫描目录下所有 .md 文件，按标题分块
    返回: (总块数, 块列表, 文件统计列表)
    """
    if not directory.exists():
        print(f"⚠️  跳过 {source_name}，路径不存在: {directory}")
        return 0, [], []

    print(f"\n📁 正在扫描 {source_name} ({directory})")
    md_files = glob.glob(str(directory / "*.md"))

    if not md_files:
        print(f"  ⚠️  未找到 .md 文件")
        return 0, [], []

    total_chunks = 0
    all_chunks = []
    file_stats = []

    for file_path in md_files:
        filename = os.path.basename(file_path)

        # 跳过忽略文件
        if filename in IGNORE_FILES:
            continue

        # 读取文件内容
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"  ❌ 读取失败 {filename}: {e}")
            continue

        # 去除首尾空白
        content = content.strip()
        if len(content) < MIN_CHUNK_SIZE:
            print(f"  ⚠️  {filename} -> 内容过短，已跳过")
            continue

        # ----- 核心分块逻辑 -----
        # 策略：优先按 Markdown 二级/三级标题（## 或 ###）分割
        # 如果无标题，则按连续空行（段落）分割
        blocks = re.split(r"\n(?=## |### )", content)

        # 如果分割后只有一块，说明文档没有二级标题，改用段落分割
        if len(blocks) <= 1:
            blocks = re.split(r"\n\n+", content)

        # 清理每个块：去除首尾空格，过滤过短的块
        cleaned_blocks = []
        for b in blocks:
            b = b.strip()
            if len(b) >= MIN_CHUNK_SIZE:
                cleaned_blocks.append(b)

        # 如果清理后依然没有有效块，将整个内容作为一块（但必须满足最小长度）
        if not cleaned_blocks and len(content) >= MIN_CHUNK_SIZE:
            cleaned_blocks = [content]

        chunk_count = len(cleaned_blocks)
        total_chunks += chunk_count
        all_chunks.extend(cleaned_blocks)
        file_stats.append({"filename": filename, "chunks": chunk_count, "size": len(content)})

        print(f"  ✅ {filename} -> {chunk_count} 个语义块")

    return total_chunks, all_chunks, file_stats


def main():
    print("=" * 55)
    print("  能量哑铃 RAG 知识库导入演示 (扫描 + 分块)")
    print("=" * 55)

    # 扫描两个目录
    core_total, core_chunks, core_stats = load_and_chunk(CORE_DIR, "01_core (核心推理库)")
    cases_total, cases_chunks, cases_stats = load_and_chunk(CASES_DIR, "02_cases (案例增强库)")

    total_chunks = core_total + cases_total
    all_chunks = core_chunks + cases_chunks
    all_stats = core_stats + cases_stats

    # ===== 输出统计报告 =====
    print("\n" + "=" * 55)
    print("📊 统计结果")
    print("-" * 55)
    print(f"  01_core 文件数: {len(core_stats)} 个")
    print(f"  01_core 语义块数: {core_total} 个")
    print(f"  02_cases 文件数: {len(cases_stats)} 个")
    print(f"  02_cases 语义块数: {cases_total} 个")
    print(f"  {'─' * 40}")
    print(f"  总文件数: {len(all_stats)} 个")
    print(f"  总语义块数: {total_chunks} 个")

    if total_chunks > 0:
        total_chars = sum(len(c) for c in all_chunks)
        avg_chunk_size = total_chars // total_chunks if total_chunks > 0 else 0
        print(f"  总文本字符数: {total_chars:,}")
        print(f"  平均每块字符数: {avg_chunk_size:,}")

    # ===== 导出样本 JSON（供人工检查分块效果）=====
    if total_chunks > 0:
        sample_file = BASE_DIR / "demo" / "chunks_sample.json"
        # 取前 10 个块作为样本（避免文件过大）
        sample_data = {
            "total_chunks": total_chunks,
            "total_files": len(all_stats),
            "samples": all_chunks[:10],
            "file_list": all_stats,
        }
        with open(sample_file, "w", encoding="utf-8") as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
        print(f"\n📄 已生成块示例文件: {sample_file}")

    # ===== 后续操作指引 =====
    print("\n" + "=" * 55)
    print("💡 下一步建议")
    print("-" * 55)
    print("  当前脚本仅做演示分块，未实际向量化入库。")
    print("  如需完整 RAG 落地，请参考以下方案：")
    print("  1. 安装依赖: pip install chromadb sentence-transformers")
    print("  2. 将上面 all_chunks 列表导入向量数据库")
    print("  3. 配合大模型 API 实现检索增强生成")
    print("=" * 55)


if __name__ == "__main__":
    main()