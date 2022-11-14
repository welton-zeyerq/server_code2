#!/usr/bin/env python3
import os
import sys
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")
try:
    import requests
except:
    sys.exit("Install missing library: pip install requests")

def helplk():
    print("follow the examples: ")
    print("")
    print("%s -h"%(sys.argv[0]))
    print("%s --help"%(sys.argv[0]))
    print("%s -u https://duckduckgo.com"%(sys.argv[0]))
    print("%s --url https://duckduckgo.com"%(sys.argv[0]))
    sys.exit()

if len(sys.argv) <=1:
    helplk()
    sys.exit()
elif len(sys.argv) ==2:
    choice = str(sys.argv[1])
    if choice == "-u":
        print("insert valid url")
        sys.exit()
    elif choice == "--url":
        print("insert valid url")
        sys.exit()
    elif choice == "-h":
        helplk()
        sys.exit()
    elif choice == "--help":
        helplk()
        sys.exit()
    else:
        print("invalid option")
        print()
        helplk()
        sys.exit()
elif len(sys.argv) >=4:
    print("invalid option")
    print()
    helplk()
    sys.exit()
else:
    pass

try:
    if __name__ == "__main__":
        url = sys.argv[2]
        response = requests.get(url)
        code = response.status_code

        if code ==100:
            print("{} [code {}] Information responses - Continue: This interim response indicates that the client should continue the request or ignore the response if the request is already finished.".format(url, code))

        elif code ==101:
            print("{} [code {}] Information responses - Switching Protocols: This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.".format(url, code))

        elif code ==102:
            print("{} [code {}] Information responses - Processing (WebDAV): This code indicates that the server has received and is processing the request, but no response is available yet.".format(url, code))

        elif code ==103:
            print("{} [code {}] Information responses - Early Hints: This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response.".format(url, code))

        elif code in range(104,199):
            print("{} [code {}] Information responses".format(url, code))

        elif code ==200:
            print("{} [code {}] Successful responses -  ok: The request succeeded. The result meaning of success depends on the HTTP method: \n GET: The resource has been fetched and transmitted in the message body. \n HEAD: The representation headers are included in the response without any message body. \n PUT or POST: The resource describing the result of the action is transmitted in the message body. \n TRACE: The message body contains the request message as received by the server. \n ".format(url, code))

        elif code ==201:
            print("{} [code {}] Successful responses - Created: The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.".format(url, code))

        elif code ==202:
            print("{} [code {}] Successful responses - Accepted: The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing. ".format(url, code))

        elif code ==203:
            print("{} [code {}] Successful responses - Non-Authoritative Information: This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status. ".format(url, code))

        elif code ==204:
            print("{} [code {}] Successful responses - No Content: There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones. ".format(url, code))

        elif code ==205:
            print("{} [code {}] Successful responses - Reset Content: Tells the user agent to reset the document which sent this request.".format(url, code))

        elif code ==206:
            print("{} [code {}] Successful responses - Partial Content: This response code is used when the Range header is sent from the client to request only part of a resource.".format(url, code))

        elif code ==207:
            print("{} [code {}] Successful responses - Multi-Status (WebDAV): Conveys information about multiple resources, for situations where multiple status codes might be appropriate.".format(url, code))

        elif code ==208:
            print("{} [code {}] Successful responses - Already Reported (WebDAV): Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.".format(url, code))

        elif code ==226:
            print("{} [code {}] Successful responses - IM Used (HTTP Delta encoding): The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.".format(url, code))

        elif code in range(227,299):
            print("{} [code {}] Successful responses".format(url, code))

        elif code ==300:
            print("{} [code {}] Redirection messages - Multiple Choices: The request has more than one possible response. The user agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)".format(url, code))

        elif code ==301:
            print("{} [code {}] Redirection messages - Moved Permanently: The URL of the requested resource has been changed permanently. The new URL is given in the response.".format(url, code))

        elif code ==302:
            print("{} [code {}] Redirection messages - Found: This response code means that the URI of requested resource has been changed temporarily. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests. ".format(url, code))

        elif code ==303:
            print("{} [code {}] Redirection messages - See Other: The server sent this response to direct the client to get the requested resource at another URI with a GET request.".format(url, code))

        elif code ==304:
            print("{} [code {}] Redirection messages - Not Modified: This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response. ".format(url, code))

        elif code ==305:
            print("{} [code {}] Redirection messages - Use Proxy: Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy. ".format(url, code))

        elif code ==306:
            print("{} [code {}] Redirection messages - unused: This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification.".format(url, code))

        elif code ==307:
            print("{} [code {}] Redirection messages - Temporary Redirect: The server sends this response to direct the client to get the requested resource at another URI with same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request. ".format(url, code))

        elif code ==308:
            print("{} [code {}] Redirection messages - Permanent Redirect: This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request.".format(url, code))

        elif code in range(309,399):
            print("{} [code {}] Redirection messages".format(url, code))

        elif code ==400:
            print("{} [code {}] Client error responses - Bad Request: The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).".format(url, code))

        elif code ==401:
            print("{} [code {}] Client error responses - Unauthorized: ".format(url, code))

        elif code ==401:
            print("{} [code {}] Client error responses - Unauthorized: Although the HTTP standard specifies unauthorized, semantically this response means unauthenticated. That is, the client must authenticate itself to get the requested response.".format(url, code))

        elif code ==402:
            print("{} [code {}] Client error responses - Payment Required: This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists. ".format(url, code))

        elif code ==403:
            print("{} [code {}] Client error responses - Forbidden: The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server. ".format(url, code))

        elif code ==404:
            print("{} [code {}] Client error responses - Not Found: The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web. ".format(url, code))

        elif code ==405:
            print("{} [code {}] Client error responses - Method Not Allowed: The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource.".format(url, code))

        elif code ==406:
            print("{} [code {}] Client error responses - Not Acceptable: This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.".format(url, code))

        elif code ==407:
            print("{} [code {}] Client error responses - Proxy Authentication Required: This is similar to 401 Unauthorized but authentication is needed to be done by a proxy.".format(url, code))

        elif code ==408:
            print("{} [code {}] Client error responses - Request Timeout: This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message. ".format(url, code))

        elif code ==409:
            print("{} [code {}] Client error responses - Conflict: This response is sent when a request conflicts with the current state of the server.".format(url, code))

        elif code ==410:
            print("{} [code {}] Client error responses - Gone: This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for limited-time, promotional services. APIs should not feel compelled to indicate resources that have been deleted with this status code. ".format(url, code))

        elif code ==411:
            print("{} [code {}] Client error responses - Length Required: Server rejected the request because the Content-Length header field is not defined and the server requires it.".format(url, code))

        elif code ==412:
            print("{} [code {}] Client error responses - Precondition Failed: The client has indicated preconditions in its headers which the server does not meet.".format(url, code))

        elif code ==413:
            print("{} [code {}] Client error responses - Payload Too Large: Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field. ".format(url, code))

        elif code ==414:
            print("{} [code {}] Client error responses - URI Too Long: The URI requested by the client is longer than the server is willing to interpret.".format(url, code))

        elif code ==415:
            print("{} [code {}] Client error responses - Unsupported Media Type: The media format of the requested data is not supported by the server, so the server is rejecting the request.".format(url, code))

        elif code ==416:
            print("{} [code {}] Client error responses - Range Not Satisfiable: The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data. ".format(url, code))

        elif code ==417:
            print("{} [code {}] Client error responses - Expectation Failed: This response code means the expectation indicated by the Expect request header field cannot be met by the server.".format(url, code))

        elif code ==418:
            print("{} [code {}] Client error responses - I'm a teapot: The server refuses the attempt to brew coffee with a teapot.".format(url, code))

        elif code ==421:
            print("{} [code {}] Client error responses - Misdirected Request: The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI. ".format(url, code))

        elif code ==422:
            print("{} [code {}] Client error responses - Unprocessable Entity (WebDAV): The request was well-formed but was unable to be followed due to semantic errors.".format(url, code))

        elif code ==423:
            print("{} [code {}] Client error responses - Locked (WebDAV): The resource that is being accessed is locked.".format(url, code))

        elif code ==424:
            print("{} [code {}] Client error responses - Failed Dependency (WebDAV): The request failed due to failure of a previous request.".format(url, code))

        elif code ==425:
            print("{} [code {}] Client error responses - Too Early: Indicates that the server is unwilling to risk processing a request that might be replayed.".format(url, code))

        elif code ==426:
            print("{} [code {}] Client error responses - Upgrade Required: The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s). ".format(url, code))

        elif code ==428:
            print("{} [code {}] Client error responses - Precondition Required:  The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict. ".format(url, code))

        elif code ==429:
            print("{} [code {}] Client error responses - Too Many Requests: The user has sent too many requests in a given amount of time (rate limiting).".format(url, code))

        elif code ==431:
            print("{} [code {}] Client error responses - Request Header Fields Too Large: The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.".format(url, code))

        elif code ==451:
            print("{} [code {}] Client error responses - Unavailable For Legal Reasons: The user agent requested a resource that cannot legally be provided, such as a web page censored by a government.".format(url, code))

        elif code in range(452,499):
            print("{} [code {}] Client error responses".format(url, code))

        elif code ==500:
            print("{} [code {}] Server error responses - Internal Server Error: The server has encountered a situation it does not know how to handle.".format(url, code))

        elif code ==501:
            print("{} [code {}] Server error responses - Not Implemented: The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.".format(url, code))

        elif code ==502:
            print("{} [code {}] Server error responses - Bad Gateway: This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.".format(url, code))

        elif code ==503:
            print("{} [code {}] Server error responses - Service Unavailable: The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached. ".format(url, code))

        elif code ==504:
            print("{} [code {}] Server error responses - Gateway Timeout: This error response is given when the server is acting as a gateway and cannot get a response in time.".format(url, code))

        elif code ==505:
            print("{} [code {}] Server error responses - HTTP Version Not Supported: The HTTP version used in the request is not supported by the server.".format(url, code))

        elif code ==506:
            print("{} [code {}] Server error responses - Variant Also Negotiates: The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.".format(url, code))

        elif code ==507:
            print("{} [code {}] Server error responses - Insufficient Storage (WebDAV): The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.".format(url, code))

        elif code ==508:
            print("{} [code {}] Server error responses - Loop Detected (WebDAV): The server detected an infinite loop while processing the request.".format(url, code))

        elif code ==510:
            print("{} [code {}] Server error responses - Not Extended: Further extensions to the request are required for the server to fulfill it.".format(url, code))

        elif code ==511:
            print("{} [code {}] Server error responses - Network Authentication Required: Indicates that the client needs to authenticate to gain network access.".format(url, code))

        elif code in range(512,599):
            print("{} [code {}] Server error responses".format(url, code))

        else:
            print("{} [code {}]".format(url, code))

except Exception as error:
    print(error)
    pass
except KeyboardInterrupt:
    sys.exit()
