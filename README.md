# Temperature Monitor & Cooling Controller (ROS 2 Python Project)

Ez a ROS 2 csomag egy hiszterézises hőmérséklet-felügyeleti és hűtésvezérlő rendszert valósít meg.
Tartalmaz két Python node-ot: egy **Publisher**-t a szimulált szenzor adatok küldéséhez és egy **Subscriber**-t az adatok fogadásához és a hűtésvezérléshez.

## Build menete

A csomag fordítása a ROS 2 munkaterületen (`~/ros2_ws`) belül történik:

1.  Helyezkedj el a munkaterület gyökerében:
    ```bash
    cd ~/ros2_ws
    ```
2.  Futtasd a `colcon build` parancsot a csomagra korlátozva:
    ```bash
    colcon build --packages-select tub_dll_random
    ```
3.  Forrásold a környezetet:
    ```bash
    source install/setup.bash
    ```

## Futtatás

Indítsd el mindkét node-ot a launch fájllal:

```bash
ros2 launch tub_dll_random cooling_system.launch.py
```

## Node-Topic kapcsolat

A rendszer egy publisher és egy subscriber node-ból áll, akik a /sensor/temperature topic-on keresztül kommunikálnak, a vezérlő pedig a /cooling/fan_state topic-on küldi a ventilátor állapotát.
```mermaid
graph TD
    subgraph tub_dll_random_pkg
        A[temp_sensor_node]
        B[cooling_controller_node]
    end

    A -->|/sensor/temperature (sensor_msgs/msg/Temperature)| B
    B -->|/cooling/fan_state (std_msgs/msg/Bool)| C[Actuator / Fan]

    style A fill:#4CAF50,color:#fff,stroke:#333
    style B fill:#FF9800,color:#fff,stroke:#333
    style C fill:#2196F3,color:#fff,stroke:#333
```
