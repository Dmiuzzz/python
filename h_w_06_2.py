class Road:
    m_asph_sq = 0.25 # в т
    thick_asph = .05 # в м
    def __init__(self, lenth, width):
        self._lenth = lenth
        self._width = width
    def calculation(self):
        m_asph_total = int(self._lenth * self._width * Road.m_asph_sq * Road.thick_asph)
        print(f"{m_asph_total}т")

my_road = Road(20, 5000)
my_road.calculation()
