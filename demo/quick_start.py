#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
demo/quick_start.py - 极简启动演示

功能说明：
1. 读取 config.json 配置
2. 加载 dist/01_core/ 中的单文件启动包
3. 通过 OpenAI 兼容 API 与大模型对话

使用方法：
1. 复制 config_example.json 为 config.json，填入你的 API 信息
2. 安装依赖：pip install requests
3. 运行：python quick_start.py

注：本脚本仅用于演示，生产环境请使用 Dify / FastGPT / LangChain 等成熟平台。
"""

import json
import requests
import os

def load_knowledge(file_path: str) -> str:
    """加载能量哑铃营销体系启动包MD知识库文本"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"知识库文件不存在：{file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def llm_chat(api_key, base_url, model, system_prompt, user_query):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.6
    }
    resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    # 1. 读取配置
    with open("config.json", "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # 2. 加载整套营销推理知识库（启动包）
    knowledge_text = load_knowledge(cfg["knowledge_file_path"])

    print("====能量哑铃营销体系 V6.2 演示Demo====")
    print("知识库加载完成，请输入企业经营问题，输入 quit 退出\n")

    while True:
        question = input("请输入问题：")
        if question.strip().lower() == "quit":
            break
        # 将整套知识库作为系统指令传入大模型
        reply = llm_chat(
            api_key=cfg["model_api_key"],
            base_url=cfg["model_base_url"],
            model=cfg["model_name"],
            system_prompt=knowledge_text,
            user_query=question
        )
        print("\n【智能体输出策略】")
        print(reply)
        print("-" * 60 + "\n")

# 注：路径中的中文文件名是正常命名，无需修改。若您的操作系统出现编码错误，请将终端编码设置为 UTF-8。