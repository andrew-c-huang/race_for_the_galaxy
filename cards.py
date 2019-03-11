class BaseCard(object):
    def __init__(self, cost, vp):
        self.cost = cost
        self.vp = vp
        self.is_military_world = False
        self.is_windfall_world = False
        self.is_production_world = False
        self.can_produce = False


class World(BaseCard):
    def __init__(self, cost, vp):
        super(World, self).__init__(cost, vp)
        self.is_world = True


class WindfallWorld(World):
    def __init__(self, cost, vp):
        super(WindfallWorld, self).__init__(cost, vp)
        self.is_windfall_world= True
        self.has_produce = True


class ProductionWorld(World):
    def __init__(self, **kw):
        super(ProductionWorld, self).__init__(**kw)
        self.is_production_world = True
        self.can_produce = True
        self.has_produce = False

    def produce(self):
        self.has_produce = True


# Military designation
class MilitaryWorld(object):
    def __init__(self):
        self.is_military_world = True


# World Types
class ConsumerWorld(object):
    def __init__(self):
        self.planet_type = 'consumer'
        self.trade_amount = 2


class MiningWorld(object):
    def __init__(self):
        self.planet_type = 'mining'
        self.trade_amount = 3


class GeneWorld(object):
    def __init__(self):
        self.planet_type = 'gene'
        self.trade_amount = 3


# Powers

class DevelopDraw(object):
    def __init__(self):
        self.develop_power = True

    def develop_activate(self):
        def __init__(self):
            self.draw_count = 1


class SettlePower(object):
    def __init__(self, settle_discount=0, military_bonus=0):
        self.settle_power = True
        self.military_bonus = military_bonus
        self.settle_discount = settle_discount


class TradePower(object):
    def __init__(self):
        self.trade_power = True


class ConsumePower(object):
    def __init__(self, consume_card_cost=1, victory_point=1, draw_card=0):
        self.is_consume = True
        self.consume_card_cost = consume_card_cost
        self.victory_point = victory_point
        self.draw_card = draw_card
        self.has_consume = False

    def consume_activate(self):
        self.has_consume = True


class ProducePower(object):
    def __init__(self, draw_card=0):
        self.produce_power = True
        self.draw_card = draw_card


class SecludedWorld(ProductionWorld, ConsumerWorld, ConsumePower):
    def __init__(self):
        ProductionWorld.__init__(self, cost=2, vp=1)
        ConsumerWorld.__init__(self)
        ConsumePower.__init__(self)
        self.name = 'secluded_world'


class WarriorRace(WindfallWorld, GeneWorld, MilitaryWorld, SettlePower):
    def __init__(self):
        WindfallWorld.__init__(self, cost=2, vp=1)
        GeneWorld.__init__(self)
        MilitaryWorld.__init__(self)
        SettlePower.__init__(self, military_bonus=1)
        self.name = 'warrior_race'




