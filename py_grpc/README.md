1. 安装依赖库 
```shell
pip install grpcio
pip install grpcio-tools  
pip install protobuf
```
2. 生成远程调用的代码
```shell
python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=. ./hello.proto

-I 指定proto所在目录
-m 指定通过protoc生成py文件
--python_out指定生成py文件的输出路径
hello.proto 输入的proto文件
```
3. 运行 TestService.py
4. 运行 TestClient.py
