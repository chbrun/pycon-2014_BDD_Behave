guard :compass

guard :shell do
    watch /(.*)\.rst/ do |m|
            `hovercraft #{m[0]} -s -t ./pycon/ ./output/`
            m[1] + " updated."
    end
    watch /pycon\/css\/(.*)\.css/ do |m|
            `hovercraft BDD_behave_Django17_pycon2014.rst -s  -t ./pycon/ ./output/`
            m[1] + " updated."
    end
end
