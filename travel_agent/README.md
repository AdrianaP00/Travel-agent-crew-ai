# Travel Agent Crew AI

Este proyecto es un agente de viaje automatizado utilizando CrewAI. El agente puede planificar actividades personalizadas, buscar restaurantes y compilar itinerarios de viaje.
## Estructura del Proyecto
```
.
├── README.md
├── knowledge
│   └── user_preference.txt
├── main.py
├── pyproject.toml
├── requirements.txt
├── src
├── travel_agent
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── main.cpython-312.pyc
│   ├── config
│   │   ├── __pycache__
│   │   │   ├── trip_agents.cpython-312.pyc
│   │   │   └── trip_tasks.cpython-312.pyc
│   │   ├── trip_agents.py
│   │   └── trip_tasks.py
│   ├── crew.py
│   └── tools
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-312.pyc
│       │   ├── browser_tool.cpython-312.pyc
│       │   ├── calculator_tool.cpython-312.pyc
│       │   └── search_tool.cpython-312.pyc
│       ├── browser_tool.py
│       ├── calculator_tool.py
│       └── search_tool.py
└── uv.lock
```

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd travel_agent
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno en el archivo [.env](http://_vscodecontentref_/14):
    ```env
    MODEL=gpt-3
    OPENAI_API_KEY=tu_api_key
    SERPER_API_KEY=tu_api_key
    BROWSERLESS_API_KEY=tu_api_key
    ```

## Uso

Para ejecutar el agente de viaje, usa el siguiente comando:
```sh
python3 travel_agent/main.py
