<!DOCTYPE html>
<html>
<head>
    <title>Chat Integration</title>
</head>
<body>

<div id="root"></div>

<!-- Include React runtime and chat component -->
<script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
<script src="/path/to/your/react-app/build/static/js/main.chunk.js"></script> <!-- Adjust the path as per your React app build -->
<script src="/path/to/your/react-app/build/static/js/2.chunk.js"></script>
<script src="/path/to/your/react-app/build/static/js/runtime-main.js"></script>

<!-- Render the chat component -->
<script>
    ReactDOM.render(
        React.createElement(ChatComponent), // Replace 'ChatComponent' with the name of your chat component
        document.getElementById('root')
    );
</script>

</body>
</html>

