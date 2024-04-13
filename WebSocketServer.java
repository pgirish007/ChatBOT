import java.io.IOException;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import javax.websocket.OnClose;
import javax.websocket.OnMessage;
import javax.websocket.OnOpen;
import javax.websocket.Session;
import javax.websocket.server.ServerEndpoint;

@ServerEndpoint("/websocket")
public class WebSocketServer {

    private static final List<Session> sessions = new CopyOnWriteArrayList<>();

    @OnOpen
    public void onOpen(Session session) {
        sessions.add(session);
        System.out.println("WebSocket opened: " + session.getId());
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        System.out.println("Message from client: " + message);
    }

    @OnClose
    public void onClose(Session session) {
        sessions.remove(session);
        System.out.println("WebSocket closed: " + session.getId());
    }

    public static void notifyAllClients(String message) {
        for (Session session : sessions) {
            try {
                session.getBasicRemote().sendText(message);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}


// WebSocketServer.notifyAllClients("Server update: some change has occurred.");
/*
 * 
 * <!DOCTYPE html>
<html>
<head>
    <title>WebSocket Example</title>
    <script>
        var socket = new WebSocket("ws://localhost:8080/your-context-path/websocket");

        socket.onopen = function(event) {
            console.log("WebSocket connection opened.");
        };

        socket.onmessage = function(event) {
            console.log("Message from server: " + event.data);
        };

        function sendMessage() {
            var message = document.getElementById("messageInput").value;
            socket.send(message);
        }
    </script>
</head>
<body>
    <h1>WebSocket Example</h1>
    <input type="text" id="messageInput" placeholder="Enter message">
    <button onclick="sendMessage()">Send</button>
</body>
</html>

 */