# The Application Context

## context lifetime(生命周期)
和 request 有 一样的 lifetime ，从 request 开始 到 request 结束

## 手动 Push a context
Application context 或 CLI command 是放置常用 data 的好地方



`g` 是 `global` 缩写

1. `get_X()` 如果资源 X 不存在，缓存为 `g.X`
2. `teardown_X()` 关闭或取消分配资源


# The Request Context

## 生命周期
当 Flask 处理一个 request ，request context 开始，同时 开始一个 application context。
当 request 结束，request context 结束，然后结束 application context.  

context 对于每一个thread(线程)都是唯一的，不能传输给其他线程，其他线程有不同的 context。  
