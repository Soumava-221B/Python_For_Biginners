def discount(price):
    '''
    Objective: To compute discount
    Input Parameter: price - numeric value
    Return Value: None
    '''
    pass

def sellingPrice(price):
    '''
    Objective: To compute selling price
    Input Parameter: price - numeric value
    Return Value: numeric value
    '''
    discountPrice = discount(price)
    if discountPrice == None:
        return price
    else:
        return discountPrice

def main():
    '''
    Objective: To compute selling price
    Input Parameter: None
    Return Value: None
    '''
    price = float(input('Enter price: '))
    print('Selling Price is', sellingPrice(price))

if __name__ == '__main__':
    main()
