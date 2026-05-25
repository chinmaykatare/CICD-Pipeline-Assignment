from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <html>
        <head><title>CI/CD Pipeline</title></head>
        <body>
            <h1>🚀 CI/CD Pipeline Working!</h1>
            <p>Assignment 19 - AWS CodePipeline</p>
            <p>Deployed via: Git → CodePipeline → CodeBuild → EC2</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print('Server running on port 8080...')
    server.serve_forever()
