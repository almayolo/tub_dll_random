# ROS 2 Hőmérséklet-felügyelet és Hűtésvezérlő Rendszer (`tub_dll_random`)

Ez a ROS 2 csomag egy hiszterézises hűtésvezérlő architektúrát valósít meg két önálló Python node segítségével.

## Architektúra és Adatfolyam

```mermaid
flowchart LR
    TNode["/temp_sensor_node"]
    CNode["/cooling_controller_node"]
    Actuator["/cooling/fan_state (Actuator)"]

    TNode -->|/sensor/temperature <br> sensor_msgs/msg/Temperature| CNode
    CNode -->|/cooling/fan_state <br> std_msgs/msg/Bool| Actuator
