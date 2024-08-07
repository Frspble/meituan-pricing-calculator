# Desc: 美团外卖商家定价计算

mt_get_percent = 0.23  #美团抽成比例（（商品原价+打包费）*抽成比例）不同地区抽成方式不同
full_discount = {   #满减优惠
    "40":3,
    "50":4,
    "70":5,
    "100":8
}
god_coupon = [20, 4]  #神券优惠，此处默认满20-4
god_coupon_percent = 0.4  #神券用户占比
god_coupon_calculate_type = 0  #神券计算方式，0-不考虑 1-算单个，2-算期望
delivery_discount = 3  #减配送费优惠

# 输入商品价格计算实际收入
product_price = eval(input('商品价格: '))
package_price = eval(input('打包费: '))
delivery_price = eval(input('配送费: '))
product_total_price = product_price + package_price  #商品总价
coupon_discount = 0  #商家对顾客的活动补贴
for key in reversed(full_discount.keys()):
    if product_total_price >= float(key):
        coupon_discount = full_discount[key]
        break
if god_coupon_calculate_type == 0:
    pass
elif god_coupon_calculate_type == 1:
    if product_total_price >= god_coupon[0]:
        coupon_discount += god_coupon[1]
elif god_coupon_calculate_type == 2:
    coupon_discount += god_coupon[1] * god_coupon_percent
discount_price = product_total_price - coupon_discount - delivery_discount  #商品优惠后金额
total_price = round(discount_price + delivery_price, 2)  #顾客实际支付
print('顾客实付:', total_price, '（商家减配送费:', delivery_discount, '商家优惠:', coupon_discount, '）', '（顾客实付中未减去第三方补贴）')
mt_service_fee = round(product_total_price * mt_get_percent, 2)  #平台服务费
print('美团净赚:', mt_service_fee)
income = round(discount_price - mt_service_fee, 2)    #商家预计收入
print('商家实收:', income)
