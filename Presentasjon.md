# Presentasjon av løsning



## Hva er brainfuck?

- Primitivt, obskurt programmeringsspråk
- Et program er en liste av operasjoner, hver operasjon er en av følgende tegn: `< > + - . , [ ]`
- `<`og  `>` brukes for å navigere seg rundt i minnet
- `-`og  `+` brukes for å minke/øke verder i minnet
- `.`og  `,` brukes for å skrive/lese karakterer i konsollen
- `[` og `]` brukes for å definere løkker

### Eksempel, Hei

For å lage ett program som skriver ut `Hei`, så er det greit å vite at hver bokstav er representert med et tall (følger ascii tabellen)

```
72   101  105
H    e    i
```

Brainfuck kode som gjør dette er feks (`python src/interpreter.py examples/hei.txt`)

```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
>
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
```


Eller litt mer konsist (`python src/interpreter.py examples/hei2.txt`)

```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
+++++++++++++++++++++++++++++.
++++.
```

### Eksempel, Hello world!

Kan gjøres enda smartere ved å bruke løkker! `Hello world!`-eksempelet blir da forholdsvis kort og obskurt (`python src/interpreter.py examples/helloworld.txt`)

```
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```


## Reward funksjon

Kalkulerer en reward basert på flere faktorer, blant annet likhet i antall printede karakterer, hvilke karakterer som ble printet og rekkefølgen på de.

Noen eksempler:

- `python src/agent.py "" "Hello world"` -> 0.0
- `python src/agent.py "H" "Hello world"` -> 3.0
- `python src/agent.py "Hw" "Hello world"` -> 5.0
- `python src/agent.py "Hwaaaaaa" "Hello world"` -> 11.0
- `python src/agent.py "Hwaa wrl" "Hello world"` -> 14.0
