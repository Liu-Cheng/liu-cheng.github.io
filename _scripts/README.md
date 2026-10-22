# 论文列表生成

`_pages/publications.md` 由 `files/publications.bib` 静态生成（原先用 BibBase 外部脚本，在部分网络下加载失败）。

新增论文后重新生成：

```bash
python3 _scripts/gen_publications.py files/publications.bib _pages/publications.md
```
