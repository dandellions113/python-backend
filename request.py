import http.client
import json
conn = http.client.HTTPSConnection("3677-2409-40d1-1a-2344-1455-b3ea-956c-a5f.ngrok-free.app",timeout=100)
payload = ''
headers = {
  'ngrok-skip-browser-warning': 'hello'
}
def main():
  conn.request("GET", "/user/?user=%22H%22", payload, headers)
  res = conn.getresponse()
  data = res.read()
  # print(data)
  # print(res.status)
  fin=data.decode("utf-8")
  print(type(fin))
  return fin
if __name__ == '__main__':
  main()