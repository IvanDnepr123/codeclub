############## Functions ############
require 'date'
def filter_by_name (name)
   return $books.filter{|t| t[:name]== name }
end 


def filter_by_avtor (avtor)
    return $books.filter{|t| t[:avtor]== avtor }
end 


def filter_by_age (age)
    return $books.filter{|l|  l[:рік_написання].to_i - age > 0 }
end


def group_by_zhanr ()
   a=$books.reduce({}) do |acc, l|
       acc[l[:zhanr]] ||= []
       acc[l[:zhanr]] << l
       acc
   end      
   return a
end


def filter_by_reiting (status)
   return $books.filter { |l| l[:reiting]=='5'}
end
############## Program ############
$books = [
  { name: 'Детектив носик і викрадачі', avtor: 'Marian Orton', рік_написання: '1973', zhanr: 'detektive', reiting: '5'},
  { name: 'Як детектив Носик здивував Нові липки', avtor: 'Marian Orton', рік_написання: '1976' , zhanr: 'detektive', reiting: '4'},
  { name: 'Як зайчик перезимував', avtor: 'Romaniuta Ivan', рік_написання: '2016' , zhanr: 'adventure', reiting: '5'},
  { name: 'Алгебра 8 клас', avtor: 'Аркадий Мерзляк', рік_написання: '2021' , zhanr: 'textbook', reiting: '4'},
  { name: 'Гаррі Поттер і філософський камінь', avtor: 'J. K. Rowling', рік_написання: '1997' , zhanr: 'fantastic', reiting: '3'},
  { name: 'Остання пригода детектива Носика', avtor: 'Marian Orton', рік_написання: '1968', zhanr: 'detektive', reiting: '4' },
  { name: 'Я, Победа і Берлін', avtor: 'Andrij Kuzmenko', рік_написання: '2006' , zhanr: 'adventure', reiting: '5'},
  { name: 'Я, паштет і армія', avtor: 'Andrij Kuzmenko', рік_написання: '2005' , zhanr: 'adventure', reiting: '3'},
]

 
puts "@@@@@@@@@@@@@@@@@@@@ Test 1 @@@@@@@@@@@@@@@@@@@@"
puts filter_by_name 'Як зайчик перезимував'
puts "@@@@@@@@@@@@@@@@@@@@ Test 2 @@@@@@@@@@@@@@@@@@@@" 
puts filter_by_age 2000
puts "@@@@@@@@@@@@@@@@@@@@ Test 3 @@@@@@@@@@@@@@@@@@@@"
puts filter_by_avtor 'Andrij Kuzmenko'
puts "@@@@@@@@@@@@@@@@@@@@ Test 4 @@@@@@@@@@@@@@@@@@@@"
puts group_by_zhanr
puts "@@@@@@@@@@@@@@@@@@@@ Test 5 @@@@@@@@@@@@@@@@@@@@"
puts filter_by_reiting '5'


