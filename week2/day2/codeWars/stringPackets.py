class InstructiongPacket:
    def __init__(self, packet:str) -> None:
        if len(packet) != 20:
            raise Exception("Illegal packet length")
        self.header = packet[0: 4]
        self.instruction = packet[4: 8]
        self.dataOne = int(packet[8: 12])
        self.dataTwo = int(packet[12: 16])
        self.footer = packet[16: 20]
        if not self.instruction in ["0F12", "B7A2", "C3D9"]:
            raise Exception("Unknown instruction")
        
    def respond(self): 
        data = ""
        value = 0
        if self.instruction == "0F12":
            value = self.dataOne + self.dataTwo
        if self.instruction == "B7A2":
            value = self.dataOne - self.dataTwo
        if self.instruction == "C3D9":
            value = self.dataOne * self.dataTwo
        # clamp the value to 4 characters
        if value < 0:
            value = 0
        elif value > 9999:
            value = 9999
        # generate the exactly 4 charater long string from the value
        data = str(value)
        while len(data) < 4:
            data = f'0{data}'
        # return the formated response packet string
        return f'{self.header}FFFF{data}0000{self.footer}'
    
someInstructionPacket = InstructiongPacket("H1H10F1200120008F4F4")
print(someInstructionPacket.respond())