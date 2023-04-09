puts "Введіть значення a, b та c для квадратного рівняння ax^2 + bx + c = 0"
a = gets.chomp.to_f 
b = gets.chomp.to_f 
c = gets.chomp.to_f 

if a == 0
  puts "Це не квадратне рівняння"
else
  discriminant=b**2 - 4*a*c
  if discriminant < 0
    puts "Дійсних коренів немає"
  else
    x1 = (-b + Math.sqrt(discriminant)) / (2*a)
    x2 = (-b - Math.sqrt(discriminant)) / (2*a)
    puts "Корені рівняння: x1 = #{x1}, x2 = #{x2}"
  end
end