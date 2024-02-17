# Kimi Chat API Simple
## KimiChat And About
KimiChat是一个效果较好的AI大模型  
此项目将此AI的API进行了封装  
方便各位开发者更快的调用
### KimiChat：https://kimi.moonshot.cn/  
## Use
在 `ApiFunc.py` 中定义了一个函数  
`chat(string:text)`  
`text` 参数是向KimiAI发送的内容  
其函数的返回值就是AI的回复内容  

## Error
在调用函数中，函数返回 `None` 并且控制台报错  
请登录你的 KimiAi 账号  
F12进入控制台，输入代码  
` window.localStorage.getItem('refresh_token') `  
将 `refresh_token` 替换为 控制台返回内容