#python 实现连接 tcp 服务并写入文件

import socket
import sys

def send_file_via_tcp(host, port, file_path):
    try:
        # 创建socket连接
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        
        # 一次性读取整个文件并发送
        with open(file_path, 'rb') as f:
            data = f.read()  # 一次性读取所有内容
            s.send(data)  # 发送数据
                
        print(f"文件 {file_path} 已成功发送到 {host}:{port}")
        
    except FileNotFoundError:
        print(f"找不到文件: {file_path}")
    except Exception as e:
        print(f"发送错误: {str(e)}")
        
    finally:
        # 关闭连接
        s.close()
        
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python tcpprint.py <IP地址> <文件路径>")
        sys.exit(1)
        
    host = sys.argv[1]    # 第一个参数是IP地址
    port = 9100           # 固定使用9100端口
    file_path = sys.argv[2]  # 第二个参数是文件路径
    
    send_file_via_tcp(host, port, file_path)

