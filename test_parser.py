from game_parser import parse

def test_parse():
    test_Start()
    test_End()
    test_Teleport()
    test_Water_and_fire()
    test_Air_and_Wall()

def run_tests():
    test_parse()

def test_Start():
    """
    Test if it can parse Start correctly, includes one start and end, no start , two start
    """
    
    """
    positive case
    """
    #Test one Start and End
    x , y =  parse(['XY'])[0]
    assert x.display == 'X', 'Test one start fail'
    assert y.display == 'Y', 'Test one end fail'
    
    """
    edge case
    """
    #Test no Start
    try:
        parse(['** **\n', '*   *\n', '**Y**'])
    except ValueError as e:
        assert str(e) == str(ValueError('Expected 1 starting position, got 0.')), 'test no start fail'

    try:
        parse([])
    except ValueError as e:
        assert str(e) == str(ValueError('Expected 1 starting position, got 0.')), 'test no start fail'
    
    """
    negative case
    """
    #Test 2 Start
    try:
        parse(['**XX*\n', '*   *\n', '**Y**'])
    except ValueError as e:
        assert str(e) == str(ValueError('Expected 1 starting position, got 2.')), 'test 2 Start fail'

    print('Test start success')
def test_End():
    """
    Test if it can parse End correctly, includes no end, two end
    """

    """
    edge case
    """
    #Test no End
    try:
        parse(['**X**\n', '*   *\n', '** **'])
    except ValueError as e:
        assert str(e) == str(ValueError('Expected 1 ending position, got 0.')), 'test no End fail'
    
    """
    negative case
    """
    #Test 2 End
    try:
        parse(['**X**\n', '*   *\n', '**YY*'])
    except ValueError as e:
        assert str(e) == str(ValueError('Expected 1 ending position, got 2.')), 'test 2 End fail'

    print('Test end success')
def test_Teleport():
    """
    Test if it can parse teleport correctly, includes 1 teleport , 2 teleport, not matching pads, too many matching pads and 0, unknown letter
    """
    
    """
    positive case
    """
    #Test one teleport
    result = parse(['X11Y'])
    teleport_1, teleport_2 = result[0][1], result[0][2]
    assert teleport_1.display == '1', 'Test one matching pad fail'
    assert teleport_2.display == '1', 'Test one matching pad fail'
    
    #Test 2 teleport
    result = parse(['X1122Y'])
    teleport_1, teleport_2 =result[0][1], result[0][2]
    teleport_3, teleport_4 =result[0][3], result[0][4]
    assert teleport_1.display == '1', 'Test 2 Teleport fail'
    assert teleport_2.display == '1', 'Test 2 Teleport fail'
    assert teleport_3.display == '2', 'Test 2 Teleport fail'
    assert teleport_4.display == '2', 'Test 2 Teleport fail'
    
    """
    negative case
    """
    #Test no matching pad
    try:
        parse(['**X**\n', '*1  *\n', '**Y**'])
    except ValueError as e:
        assert str(e) == str(ValueError('Teleport pad 1 does not have an exclusively matching pad.')), 'test no matching pad fail'
    
    #Test bad unknown letter
    try:
        parse(['**X**\n', '*Joe*\n', '**Y**'])
    except ValueError as e:
        assert str(e) == str(ValueError('Bad letter in configuration file: J.')), 'test bad unknown letter fail'
    
    """
    edge case
    """
    #Test bad letter 0
    try:
        parse(['**X**\n', '* 0*\n', '**Y**'])
    except ValueError as e:
        assert str(e) == str(ValueError('Bad letter in configuration file: 0.')), 'test bad letter 0 fail'
    
    #Test too many matching pad
    try:
        parse(['**X**\n', '*111*\n', '**Y**'])
    except ValueError as e:
        assert str(e) == str(ValueError('Teleport pad 1 does not have an exclusively matching pad.')), 'test too many matching pad fail'

    print('Test teleport success')
def test_Water_and_fire():
    """
    Test if it can parse water and fire, includes one and two water and fire
    """
    
    """
    positive case
    """
    #Test one water and fire
    result = parse(['XWFY'])
    water, fire = result[0][1], result[0][2]
    assert water.display == 'W', 'Test one water fail'
    assert fire.display == 'F', 'Test one fire fail'

    #Test 2 water and fire
    result = parse(['XWWFFY'])
    water1, water2 = result[0][1], result[0][2]
    fire1, fire2 = result[0][3], result[0][4]
    assert water1.display == 'W', 'Test one water fail'
    assert water2.display == 'W', 'Test one water fail'
    assert fire1.display == 'F', 'Test one fire fail'
    assert fire2.display == 'F', 'Test one fire fail'
    
    print('Test water and fire success')
def test_Air_and_Wall():
    """
    Test if it can parse air and wall
    """
    
    """
    positive case
    """
    result = parse(['X *Y'])
    air = result[0][1]
    wall = result[0][2]
    assert air.display == ' ', 'Test air fail'
    assert wall.display == '*', 'Test wall fail'
    print('Test air and wall success')