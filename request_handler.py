import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import closerange
from posts.request import create_post, get_single_post
from users import create_user
from users import get_all_users
from users import get_single_user
from users import check_user
from categories import get_single_category, get_all_categories,create_category
from comments import create_new_comment, get_all_comments, get_single_comment
from tags import get_all_tags
from tags  import create_tag
from posts import get_all_posts, get_single_post, create_post

class HandleRequests(BaseHTTPRequestHandler):

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:
            # What is happening with both the param and the resource being split
            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return (resource, key, value)

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

            return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            (resource, id) = parsed

            if resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"

                else:
                    response = f"{get_all_users()}"

            elif resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"

            elif resource == "comments":
                if id is not None:
                    response = f"{get_single_comment(id)}"
                else:
                    response = f"{get_all_comments()}"
            elif resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"

            elif resource == "tags":
                if id is not None:
                    response = f"{get_single_tag(id)}"
                else:
                    response = f"{get_all_tags()}"

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        # Counts number of characters from request
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_resource = None

        if resource == "users":
            new_resource = f"{create_user(post_body)}"
        
        elif resource == "login":
            new_resource = f"{check_user(post_body)}"

        elif resource == "comments":
            new_resource = create_new_comment(post_body)

        elif resource == "categories":
            new_resource = create_category(post_body)

        elif resource == "newPost":
            new_resource = create_post(post_body)
        
        elif resource == "tags":
            new_resource = create_tag(post_body)

        self.wfile.write(f"{new_resource}".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
