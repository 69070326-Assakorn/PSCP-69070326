"""boba"""
boba_type,boba_mass=input().split()
tea_type,sweet_level,tea_cc=input().split()
boba_mass=float(boba_mass)
tea_cc=float(tea_cc)
energy=0
match boba_type:
    case 'H':
        energy+=5*boba_mass
    case 'O':
        energy+=3*boba_mass
    case 'J':
        energy+=2*boba_mass
match tea_type:
    case 'R':
        match sweet_level:
            case '1':
                energy+=12*tea_cc
            case '2':
                energy+=18*tea_cc
            case '3':
                energy+=25*tea_cc
    case 'T':
        match sweet_level:
            case '1':
                energy+=15*tea_cc
            case '2':
                energy+=20*tea_cc
            case '3':
                energy+=30*tea_cc
    case 'M':
        match sweet_level:
            case '1':
                energy+=10*tea_cc
            case '2':
                energy+=15*tea_cc
            case '3':
                energy+=20*tea_cc
print(f'{energy:g}')
