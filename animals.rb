animals = [
    { 'name' => 'Dragon Toothless', 'color' => 'black', 'eyeColor' => 'black',  'weight' => 300},
    { 'name' => 'Dog Patron', 'color' => 'brown', 'eyeColor' => 'black', 'weight' => 7},
    { 'name' => 'Cat Crookshanks', 'color' => 'orange', 'eyeColor' => 'brown', 'weight' => 12},
    { 'name' => 'Owl Hedwig', 'color' => 'white', 'eyeColor' => 'yellow', 'weight' => 5},
    { 'name' => 'Panda Po', 'color' => 'black and white', 'eyeColor' => 'black', 'weight' => 322},
    { 'name' => 'Lion Simba', 'color' => 'yellow', 'eyeColor' => 'brown', 'weight' => 24},
    { 'name' => 'Cat Garfild', 'color' => 'orange', 'eyeColor' => 'green', 'weight' => 18},
    { 'name' => 'Dog Dante', 'color' => 'grey', 'eyeColor' => 'yellow', 'weight' => 12},
    { 'name' => 'Cock Hey-Hey', 'color' => 'yellow, green, red', 'eyeColor' => 'green', 'weight' => 3},
    { 'name' => 'Sponge Bob', 'color' => 'yellow', 'eyeColor' => 'brown', 'weight' => 2},
    { 'name' => 'Winnie bear', 'color' => 'yellow', 'eyeColor' => 'black, white', 'weight' => 12},
    { 'name' => 'Busya rat', 'color' => 'grey, white, black', 'eyeColor' => 'black', 'weight' => 0.300}
]

puts "- Я хочу собі невелику тваринку. Чия вага від 5 до 10 кг"
animals.each do |an|
    if an["weight"]>=5 and an["weight"]<=10
        puts "#{an['name']}    #{an["weight"]}"
    end
end    
puts "- Я хочу великого улюбленця більше 100 кг і що він був чорного кольору, або повністю або частково"
animals.each do |an|
    if an["weight"]>=100 and an["color"].include?'black'
        puts "#{an['name']}    #{an["weight"]}"
    end
end  
puts "- Я хочу улюбленця з чорними або коричневими очима"
animals.each do |an|
    if an["eyeColor"]=='black' or an["eyeColor"]=='brown'
        puts "#{an['name']}    #{an["eyeColor"]}"
    end
end  
puts "- Мені підійде будь-яка тваринка, крім кота"
animals.each do |an|
    if !an["name"].include? 'Cat'
        puts "#{an['name']}"
    end
end 
puts "- Можна мені собаку або панду?"
animals.each do |an|
    if an["name"].include? 'Dog' or an["name"].include? 'Panda'
        puts "#{an['name']}"
    end
end
puts "- Я хочу тваринку до 30 кг. І щоб у неї були очі чорного чи коричневого кольору"
animals.each do |an|
    if an["weight"]<=30 and an["eyeColor"]== 'brown' or an["weight"]<=30 and an["eyeColor"]== 'black'
        puts "#{an['name']} #{an['weight']} #{an['eyeColor']}"
    end
end
puts "- Я хочу кота. Але не з коричневими очима"
animals.each do |an|
    if an["name"].include? 'Cat' and an["eyeColor"] != 'brown'
        puts "#{an['name']} #{an['eyeColor']}"
    end
end
puts "- Я хочу Вежмежатко жовтого кольору."
animals.each do |an|
    if an["name"].include? 'bear' and an["color"] == 'yellow'
        puts "#{an['name']} #{an['eyeColor']}"
    end
end
puts "- Я хочу розумну криску."
animals.each do |an|
    if an["name"].include? 'rat'
        puts "#{an['name']} "
    end
end