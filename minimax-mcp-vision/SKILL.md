---
name: minimax-mcp-vision
description: 使用 MiniMax Coding Plan MCP 进行图片理解与分析。当用户需要分析图片内容、识别图片中的物体、描述图片场景、理解图片含义时使用此技能。支持图片问答、物体识别、场景描述等。
---

# MiniMax MCP 图片理解

使用 MiniMax Coding Plan MCP 的 understand_image 工具进行图片分析。

## 环境配置

- 需要设置 `MINIMAX_API_KEY` 环境变量 (MiniMax Coding Plan API Key)
- 或使用 `--api-key` 参数直接传入 API Key

## 使用方法

```bash
cd ~/.npm-global/lib/node_modules/openclaw/skills/minimax-mcp-vision
source .venv/bin/activate
export http_proxy=http://192.168.31.32:15732
export https_proxy=http://192.168.31.32:15732
python scripts/analyze_image.py -i /path/to/image.jpg -p "请描述这张图片"
```

## 参数说明

- `-i, --image`: 图片路径 (必需)
- `-p, --prompt`: 提示词，默认 "请描述这张图片"
- `-k, --api-key`: API Key (可选，默认从环境变量读取)
- `-o, --output`: 输出文件路径 (可选)

## 示例

```bash
# 描述图片内容
python scripts/analyze_image.py -i photo.jpg -p "这张图片里有什么?"

# 识别物体
python scripts/analyze_image.py -i photo.jpg -p "图片中有哪些物体?"

# 分析场景
python scripts/analyze_image.py -i photo.jpg -p "描述这个场景"
```
