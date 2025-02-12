# Mustererkennung / Reg. Ausdr.
Projektarbeit Python 2025-I

## Ziele: 

Möglichst viele bisher behandelte Aspekte von Python wiederholen

- Klassen definieren und Objekte nutzen
- RegEx (reguläre Ausdrücke ) - Erkennen von Mustern in Texten (zunächst nur deutsch)



- Verzicht auf alle Erweiterungen, die nicht zur <b>Python Standard Library</b> gehören

## Programmablauf

```mermaid

sequenceDiagram
    Bot->User: Welcome message
    loop until 'quit'
        Bot-->User: message
        User-->Bot: message
    end

```



## Beispiel-Dialog

```mermaid

sequenceDiagram
    Bot ->> User: Guten Tag, ich heisse Dr. Seltsam. Wie kann ich dir helfen?
    Note right of User: Beispieldialog
    User--x Bot: Hallo bot, wie geht es Dir?
    Bot ->> User: Sehr gut, danke. Und wie läuft es bei dir?
    User-->Bot: Mir geht es gut, danke!
    
    
```