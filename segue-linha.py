
def control(left_sensor, right_sensor, speed):
    if (left_sensor == right_sensor):
        torque = 5000 
        valor = 0
    else:
        torque = 2200

    if speed >= 122.2 and left_sensor != right_sensor:
        valor = 0.5635
 
    else: 
        valor = 0.3
    if left_sensor == 0.00 or right_sensor == 0.00:
        torque = 2500
        
    
    P = valor
    erro = right_sensor - left_sensor
    
    return {
        'engineTorque': torque,
        'brakingTorque': 0,
        'steeringAngle': P * erro,
        'log': [
            { 'name': 'Speed', 'value': speed, 'min': 0, 'max': 200 },
            { 'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            { 'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1 }
        ]
    }

