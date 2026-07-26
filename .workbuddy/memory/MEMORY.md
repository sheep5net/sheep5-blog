# Sheep5 博客项目记忆

## 博客信息
- 域名：https://sheep5.net
- 技术栈：Hugo + PaperMod 主题
- 部署：GitHub（sheep5net/sheep5-blog）→ Cloudflare Pages 自动构建
- 构建命令：`hugo --gc --minify`，输出目录 `public`
- Hugo 版本：v0.164.0 extended
- www.sheep5.net → 301 重定向到 sheep5.net（Cloudflare Redirect Rules）

## 文章发布工作流
1. 用户在 Obsidian「需要发布的文章」文件夹写文章
2. 路径：`iCloud~md~obsidian/Documents/匡文成的笔记本/需要发布的文章/`
3. 文件名格式：`2026年7月20日 标题.md`
4. 转换规则：
   - 发布时间 = 文件创建时间（`stat -f "%SB"`）
   - 去掉标题开头的日期前缀（如「2026年7月20日 」）
   - 生成 5 位随机数字 slug
   - 使用 Page Bundle 模式：每篇文章一个专属文件夹 `content/posts/<slug>/`
   - 文件夹内放 `index.md`（文章）和所有图片
   - 图片压缩：宽度不超过 1200px，JPEG 质量 80%，用 `sips` 处理
   - Obsidian 图片引用 `![[image.png]]` 转为标准 Markdown `![alt](image.png)`
   - Obsidian 图片引用 `![alt](attachments/image.png)` 转为 `![alt](image.png)`
   - 确保所有图片在 Hugo 中正常显示
5. 文章 front matter 用 archetype 模板（`archetypes/default.md`）
6. 推送到 GitHub，Cloudflare Pages 自动部署

## 配置要点
- 固定链接：`/posts/:slug/`（5位随机数字）
- 标题分隔符：`-`（覆盖了 PaperMod 的 head.html）
- 中文界面（i18n/zh-cn.yaml）
- RSS：`/rss.xml`，限 5 篇
- Sitemap：daily
- 社交图标：RSS
- 首页无欢迎语
