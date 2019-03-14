class BaseCard(object):
    def __init__(self, cost, vp):
        self.cost = cost
        self.vp = vp

        self.is_military_world = False
        self.is_windfall_world = False
        self.is_production_world = False
        self.can_produce_good = False
        self.has_produce_good = False

        self.has_explore_power = False
        self.has_develop_power = False
        self.has_settle_power = False
        self.has_trade_power = False
        self.has_consume_power = False
        self.has_produce_power = False


class Development(BaseCard):
    def __init__(self, cost, vp):
        super(Development, self).__init__(cost, vp)
        self.is_development = True


class World(BaseCard):
    def __init__(self, cost, vp):
        super(World, self).__init__(cost, vp)
        self.is_world = True


class WindfallWorld(World):
    def __init__(self, cost, vp):
        super(WindfallWorld, self).__init__(cost, vp)
        self.is_windfall_world= True
        self.has_produce_good = True


class ProductionWorld(World):
    def __init__(self, **kw):
        super(ProductionWorld, self).__init__(**kw)
        self.is_production_world = True
        self.can_produce_good = True


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

class ExplorePower(object):
    def __init__(self, draw_extra=0, keep_extra=0):
        self.is_explore_power = True
        self.draw_extra = draw_extra
        self.keep_extra = keep_extra


class DevelopPower(object):
    def __init__(self, draw=0, reduce_cost=0, draw_after=0):
        self.is_develop_power = True
        self.draw=draw
        self.reduce_cost = reduce_cost
        self.draw_after = draw_after


class SettlePower(object):
    def __init__(self, reduce_cost=0, specific_reduce_cost={}, reduce_cost_to_0=[], military=0, specific_military={},
                 temporary_military=0, pay_for_military=0, draw_after=0):
        self.is_settle_power = True
        self.reduce_cost = reduce_cost
        self.specific_reduce_cost = specific_reduce_cost
        self.reduce_cost_to_0 = reduce_cost_to_0
        self.military = military
        self.specific_military = specific_military
        self.temporary_military = temporary_military
        self.pay_for_military = pay_for_military
        self.draw_after = draw_after

class TradePower(object):
    def __init__(self, any_good=0, specific_kind_of_good={}, this_worlds_good=0):
        self.is_trade_power = True
        self.any_good = any_good
        self.specific_kind_of_good = specific_kind_of_good
        self.this_worlds_good = this_worlds_good


class ConsumePower(object):
    def __init__(self, consume_card_cost=1, victory_point=1, discard_up_to=1, draw_card=0, card_at_trade_price=False):
        self.is_consume_power = True
        self.consume_card_cost = consume_card_cost
        self.victory_point = victory_point
        self.draw_card = draw_card
        self.has_consume = 0
        self.discard_up_to = discard_up_to
        self.card_at_trade_price = card_at_trade_price

    def consume_activate(self):
        self.has_consume = self.discard_up_to
# special class for all goods, different kind of goods, and specific kind of goods

class ProducePower(object):
    def __init__(self, produce_good=False, produce_windfall_good=False, produce_specific_windfall=[],
                 draw=0, produce_good_and_draw=False, draw_on_produced_windfall=False, draw_for_worlds=[],
                 draw_for_most_of_a_kind=[], draw_for_different_kinds=False):
        self.is_produce_power = True
        self.produce_good = produce_good,
        self.produce_windfall_good = produce_windfall_good,
        self.produce_specific_windfall = produce_specific_windfall
        self.draw = draw
        self.produce_good_and_draw = produce_good_and_draw
        self.draw_on_produced_windfall = draw_on_produced_windfall
        self.draw_for_worlds = draw_for_worlds
        self.draw_for_most_of_a_kind = draw_for_most_of_a_kind
        self.draw_for_different_kinds = draw_for_different_kinds
        self.has_produce_good = False

    def produce_activate(self):
        self.has_produce_good = True


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
        SettlePower.__init__(self, military=1)
        self.name = 'warrior_race'


class ExpeditionForce(Development, ExplorePower, SettlePower):
    def __init__(self):
        Development.__init__(self, cost=1, vp=1)
        ExplorePower.__init__(self, draw_extra=1)
        SettlePower.__init__(self, military=1)
        self.name = 'expedition_force'

class InvestmentCredits(Development, ExplorePower, DevelopPower):
    def __init__(self):
        Development.__init__(self, cost=1, vp=1)
        DevelopPower.__init__(self, reduce_cost=1)
        self.name = 'investment_credits'

