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
flowchart LR
    TNode["/temp_sensor_node<br><i>(Hőmérséklet szimulátor)</i>"]
    CNode["/cooling_controller_node<br><i>(Hiszterézises vezérlő)</i>"]
    Actuator["/cooling/fan_state<br><i>(Ventilátor beavatkozó)</i>"]

    TNode -->|/sensor/temperature <br> <b>sensor_msgs/msg/Temperature</b>| CNode
    CNode -->|/cooling/fan_state <br> <b>std_msgs/msg/Bool</b>| Actuator
