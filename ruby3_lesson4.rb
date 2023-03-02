puts "Number 1:"
a1 = gets.chomp.to_i
puts "Number 2:"
a2 = gets.chomp.to_i
puts "(+ or - or * or /) without spase"
a3 = gets.chomp.to_s
if a3 == "+"
    puts  "#{a1} + #{a2} = #{a1+a2}" 
elsif a3 == "-"
    puts  "#{a1} - #{a2} = #{a1-a2}" 
elsif a3 == "*"
    puts  "#{a1} * #{a2} = #{a1*a2}" 
elsif a3 == "/"
    puts  "#{a1} / #{a2} = #{a1/a2}" 
else
    puts "???"
end

