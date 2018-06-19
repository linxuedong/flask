# The Application Context

## context lifetime(生命周期)
和 request 有 一样的 lifetime ，从 request 开始 到 request 结束

## 手动 Push a context
Application context 或 CLI command 是放置常用 data 的好地方



`g` 是 `global` 缩写

1. `get_X()` 如果资源 X 不存在，缓存为 `g.X`
2. `teardown_X()` 关闭或取消分配资源
