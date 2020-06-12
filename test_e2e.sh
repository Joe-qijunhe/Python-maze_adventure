#! /usr/bin/env sh
echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################\n"
count=0 # number of test cases run so far

# Assume all `.in` and `.out` files are located in a separate `tests_e2e` directory

for folder in `ls -d tests_e2e/* | sort -V`; do
    name=$(basename "$folder")
    
    echo Running test $name.

    config_file=tests_e2e/$name/$name.config
    expected_file=tests_e2e/$name/$name.out
    in_file=tests_e2e/$name/$name.in

    # Change this command to run your program!
    # You will need to read the code here and figure out how to pass in your config yourself!
    python3 run.py $config_file < $in_file | diff - $expected_file || echo "Test $name: failed!\n"

    count=$((count+1))
done

echo "Finished running $count tests!"