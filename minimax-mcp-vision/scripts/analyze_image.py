#!/usr/bin/env python3
"""
MiniMax MCP Vision - 图片理解
使用 MiniMax Coding Plan MCP 进行图片分析
"""

import os
import sys
import asyncio
import argparse
from mcp import ClientSession
from mcp.client.stdio import stdio_client

def analyze_image(image_path: str, prompt: str, api_key: str = None) -> str:
    """使用 MiniMax MCP understand_image 工具分析图片"""
    
    if api_key is None:
        api_key = os.environ.get("MINIMAX_API_KEY")
    
    if not api_key:
        print("Error: 请设置 MINIMAX_API_KEY 环境变量或传入 api_key 参数", file=sys.stderr)
        sys.exit(1)
    
    # 绝对路径
    abs_path = os.path.abspath(image_path)
    
    # 环境变量
    env = os.environ.copy()
    env["MINIMAX_API_KEY"] = api_key
    env["MINIMAX_API_HOST"] = "https://api.minimaxi.com"
    
    return asyncio.run(_analyze(abs_path, prompt, env))

async def _analyze(image_path: str, prompt: str, env: dict) -> str:
    """异步调用 MCP"""
    
    from mcp.client.stdio import StdioServerParameters
    
    server_params = StdioServerParameters(
        command="uvx",
        args=["minimax-coding-plan-mcp", "-y"],
        env=env
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化
            await session.initialize()
            
            # 调用工具
            result = await session.call_tool(
                "understand_image",
                {
                    "prompt": prompt,
                    "image_source": image_path
                }
            )
            
            # 解析结果
            if result.content:
                for block in result.content:
                    if block.type == "text":
                        return block.text
            
            return str(result)

def main():
    parser = argparse.ArgumentParser(description="MiniMax MCP 图片理解")
    parser.add_argument("--image", "-i", required=True, help="图片路径")
    parser.add_argument("--prompt", "-p", default="请描述这张图片", help="提示词")
    parser.add_argument("--api-key", "-k", help="API Key (可选，默认从环境变量读取)")
    parser.add_argument("--output", "-o", help="输出文件路径 (可选)")
    
    args = parser.parse_args()
    
    result = analyze_image(args.image, args.prompt, args.api_key)
    
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"结果已保存到: {args.output}")
    else:
        print(result)

if __name__ == "__main__":
    main()
