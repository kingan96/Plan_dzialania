class beam(object):
    def __init__(self, length=1, width=0.5, height=0.5, force=10, 
                 position_force=0.5, material='concrete'):
        self.length = length
        self.width = width
        self.height = height
        self.force = force
        self.position_force = position_force
        self.material = material
        
    def moment(self):
        pf=self.position_force
        Mmax = (pf*(self.length-pf)*self.force(self.length))
        return Mmax
   
    beam(length, width, height, material)
    beam = Beam()
    sb = Beam(height=0.3)
    a = sb.moment()
