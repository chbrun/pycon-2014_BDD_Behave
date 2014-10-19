guard :compass

guard :shell do
    watch /(.*)\.rst/ do |m|
            `hovercraft #{m[0]} -s -t ./pycon/ ./output/`
            m[1] + " updated."
    end
    watch /css\/(.*)\.css/ do |m|
            `hovercraft #{m[1]}.rst -s  -t ./pycon/ ./output/`
            m[1] + " updated."
    end
end
