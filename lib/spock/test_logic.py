from spock import *

def test_basic():
    Farmer = predicate.Farmer
    Rabbit = predicate.Rabbit
    Hates  = predicate.Hates
    Wife  = predicate.Wife
    Mac = symbol.Mac
    Pete = symbol.Pete
    print (Farmer(Mac) & Rabbit(Pete) >> Hates(Mac,Pete))

    kb0 = Doctrine( [ Farmer(Mac),
                      Rabbit(Pete),
                      ( Rabbit(s.r) &
                        Farmer(s.f) ) >>
                      Hates(s.f, s.r) ] )


    kb0.tell(Rabbit(s.Flopsie))

    # Flopsie
    print kb0.ask(Hates(Mac, s.x))[s.x]

    # should be False
    print kb0.ask(Wife(Pete, s.x))

    # should be [Pete, Flopsie]
    all_solutions = kb0.consider(Hates(Mac, s.x), s.x)
    print [z for z in all_solutions]

def test_theta():
    import datetime
    t = datetime.datetime.now()
    alice,bob,action = 'one','two','three'
    print Obligation(alice, bob, t, action)

if __name__=='__main__':
    test_basic()
    test_theta()
    from IPython import Shell; Shell.IPShellEmbed(argv=['-noconfirm_exit'])()
