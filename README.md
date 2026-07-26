# 我的 Hugo 博客

基于 Hugo + PaperMod 主题，部署在 Cloudflare Pages。

## 本地预览

```bash
hugo server -D
```

浏览器打开 http://localhost:1313

## 构建

```bash
hugo --gc --minify
```

构建产物在 `public/` 目录。

## Cloudflare Pages 部署配置

| 项目 | 值 |
|------|-----|
| 构建命令 | `hugo --gc --minify` |
| 输出目录 | `public` |
| 环境变量 | `HUGO_VERSION` = `0.164.0` |

## 目录结构

```
├── content/          # 文章内容
│   ├── posts/        # 博客文章
│   ├── archives/     # 归档页
│   └── search/       # 搜索页
├── themes/PaperMod/  # 主题（git submodule）
├── hugo.toml         # 站点配置
└── static/           # 静态资源（图片等）
```

## 写文章

```bash
hugo new content/posts/文章名.md
```
