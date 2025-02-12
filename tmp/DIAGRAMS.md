```mermaid

sequenceDiagram
    Bot->User: Welcome message
    loop until 'quit'
        Bot-->User: message
        User-->Bot: message
    end

```