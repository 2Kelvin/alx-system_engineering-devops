#!/usr/bin/env ruby
# Regex for TextMe app message transactions
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(",")
