# OneBot Standard

The OneBot standard is an abstraction of the API for developing chatbots. It standardizes the communication methods, data formats, and fields used by chatbot APIs.

The OneBot standard can be compared to specifications like C, ECMAScript, and POSIX. OneBot implementations correspond to things like GCC, Chrome V8, and Linux.

## Keywords

- **MUST** - Required
- **MUST NOT** - Prohibited
- **SHOULD** - Recommended
- **SHOULD NOT** - Not recommended
- **MAY** - Optional

The keywords follow RFC 2119.

## Overview

The OneBot standard has two parts:

- **OneBot Connect** - Specifies communication and data protocols
- **Interface Definition** - Defines events, actions, message segments

## Terminology

- **Robot/Bot** - Refers to a chatbot
- **Robot Platform** - Platforms like QQ, WeChat, Telegram that provide chatbot APIs
- **OneBot** - The OneBot standard or an implementation
- **OneBot Standard** - The OneBot chatbot API standard
- **OneBot Implementation** - A program that implements the OneBot standard
- **OneBot Application** - A program built on top of OneBot to realize chatbot logic
- **OneBot SDK** - Helpers for building OneBot applications
- **OneBot Library** - Reusable OneBot implementation code

## Events

Events represent things like messages, notifications, etc. generated within a platform. OneBot pushes them to the application.

### Event Format

Events are encoded as JSON objects with required fields:

- `id` - Unique event ID
- `time` - Event timestamp
- `type` - `meta`, `message`, `notice`, `request`
- `detail_type` - Detail type  
- `sub_type` - Subtype
- `self` - Sender identity

### Event Examples

```json
{
  "id": "123",
  "self": {
    "platform": "qq",
    "user_id": "1234"
  },
  "time": 12345,
  "type": "message",
  "detail_type": "private",
  "message_id": "456",
  "message": [
    {"type": "text","data": {
      "text": "Hello World"
    }}
  ]
}
```

## Action Requests

Action requests are sent by the application to request services from OneBot.

### Action Request Format

Action requests are encoded as JSON objects with required fields:

- `action` - Action name
- `params` - Parameters
- `self` - Sender identity

### Action Request Examples

```json
{
  "action": "send_message",
  "params": {
    "message": ["Hello World!"] 
  },
  "self": {
    "platform": "telegram",
    "user_id": "abcd1234"
  }
}
```

## Action Responses

Action responses are sent by OneBot back to the application after processing a request.

### Action Response Format

Action responses are encoded as JSON objects with required fields:

- `status` - `ok` or `failed`
- `retcode` - Return code
- `data` - Response data
- `message` - Error message

### Action Response Examples

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": "success"
  },
  "message": "" 
}
```

## Return Codes

Return codes indicate execution status:

- `0` - Success
- `1xxxx` - Request errors
- `2xxxx` - Handler errors  
- `3xxxx` - Execution errors

## Communication Methods

OneBot Connect supports:
  
- HTTP
- HTTP Webhook
- WebSocket Forward
- WebSocket Reverse

It specifies communication protocol and data encoding.

## Data Protocols

OneBot Connect uses:

- Events
- Action Requests
- Action Responses

It defines the data transmitted between the application and OneBot implementation.
Here is more of the OneBot documentation formatted with Markdown:

## HTTP Communication

OneBot runs an HTTP server based on configuration:

- `host` - Listening IP
- `port` - Listening port
- `access_token` - Authentication
- `event_enabled` - Enable event polling
- `event_buffer_size` - Event buffer size

OneBot handles requests at `/` and returns action responses.

### HTTP Authentication

If `access_token` is set, OneBot authenticates via:

- `Authorization` header
- `access_token` query parameter

### HTTP Content Types

Supported request content types:

- `application/json` (required)
- `application/msgpack` (optional)

Response `Content-Type` mirrors request.

### HTTP Event Polling

If `event_enabled` is `true`, OneBot supports `get_latest_events` to poll events.

It provides an event buffer of configurable `event_buffer_size`.

## HTTP Webhook

OneBot pushes events to a webhook URL based on configuration:

- `url` - Webhook URL
- `access_token` - Authentication
- `timeout` - Request timeout

### HTTP Webhook Headers

Required request headers:

- `Content-Type` - `application/json`
- `User-Agent` - OneBot version
- `X-OneBot-Version` - OneBot version
- `X-Impl` - OneBot implementation

Optional `Authorization` header for authentication.

### HTTP Webhook Auth

Authenticates via:

- `Authorization` header
- `access_token` query parameter

### HTTP Webhook Timeout

Request timeout is based on configured `timeout` value.

## WebSocket Communication

OneBot supports WebSocket server and client roles.

Forwards events to clients and handles action requests.

### WebSocket Authentication

If `access_token` is set, OneBot authenticates before handshake via:

- `Authorization` header
- `access_token` query parameter

### WebSocket Events & Actions

- Events as JSON
- Action requests as JSON or MessagePack
- Responses use request format  

## WebSocket Communication (cont'd)

### WebSocket Forward

OneBot runs a WebSocket server based on configuration:

- `host` - Listening IP
- `port` - Listening port  
- `access_token` - Authentication

It accepts connections at `/` and handles events and actions.

### WebSocket Reverse  

OneBot connects to a WebSocket endpoint based on configuration:

- `url` - WebSocket URL
- `access_token` - Authentication
- `reconnect_interval` - Reconnect interval

It handles events and actions after connecting.

## Data Types

| Type | Values |
|-|-|
| Integer | int64, uint64, int32, uint32, int16, uint16, int8, uint8 |
| Float | float64 |
| String | string |
| Bytes | Base64-encoded string or byte array |
| Array | any[] |
| Map | map[key_type]value_type |
| Object | object (map[string]any) |

## Action Response

Action responses are objects with required fields:

- `resp` - Action name
- `status` - Status
- `retcode` - Return code
- `data` - Response data
- `message` - Error message

## Robot Self Identification

`self` objects identify a robot:

```json
{
  "platform": "telegram",
  "user_id": "123" 
}
```

## Events

Events represent messages, notifications, etc:

### Event Format

Events are objects with required fields:

- `id` - Unique ID
- `self` - Sender identity
- `time` - Timestamp
- `type` - Event type

### Event Example

```json
{
  "id": "123",
  "self": {
    "platform": "qq",
    "user_id": "1234"
  },
  "time": 1632847927,
  "type": "message",
  
  // other fields based on type  
}
```

## Action Requests

Action requests are sent by the application to request services.

### Action Request Format

Action requests are objects with required fields:

- `action` - Action name
- `params` - Parameters

And optional:

- `echo` - Identifier
- `self` - Sender identity

### Action Request Example

```json
{
  "action": "send_message",
  "params": {
    "message": ["Hi there!"] 
  },
  "echo": "123"
}
```

## Action Responses

The action response is data sent by OneBot to the application after processing a request.

### Action Response Format

Action responses are objects with required fields:

- `status` - `ok` or `failed`
- `retcode` - Return code
- `data` - Response data
- `message` - Error message

And optional:

- `echo` - Matches request identifier

### Action Response Example

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": "success"
  },
  "echo": "123" 
}
```

## Return Codes

Return codes indicate execution status:

| Code | Meaning |  
|-|-|
| 0 | Success |
| 1xxxx | Request errors |
| 2xxxx | Handler errors |
| 3xxxx | Execution errors |

### Request Errors

Similar to HTTP 4xx client errors.

| Code | Error | Cause |
|-|-|-|
| 10001 | Bad Request | Malformed request |
| 10002 | Unsupported Action | Unimplemented action |
| 10003 | Bad Param | Invalid parameter |

And more.

### Handler Errors

Similar to HTTP 5xx server errors:

| Code | Error | Cause |
|-|-|-|  
| 20001 | Bad Handler | Implementation error |
| 20002 | Internal Handler Error | Uncaught exception |

And more.

## Action Responses

Action responses are sent back by OneBot after processing a request:

### Action Response Format

Action responses are objects with required fields:

- `status` - `ok` or `failed`  
- `retcode` - Return code
- `data` - Response data
- `message` - Error message

And optional:

- `echo` - Mirrors request identifier

### Action Response Example

```json
{
  "status": "ok",
  "retcode": 0,
  "data": {
    "result": "success"
  },
  "echo": "123"
}
```
