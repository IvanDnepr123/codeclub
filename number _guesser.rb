i = rand(0..10)
while i == i 
    puts("Відгадай моє задумане число!!!")
    u = gets.chomp.to_i
    if u == i
        puts("Ти вгадав!!! ")
        i = rand(0..10) 
    else
        puts("Невірно!!! Моє число було: #{i}")
        i = rand(0..10)
    end
end