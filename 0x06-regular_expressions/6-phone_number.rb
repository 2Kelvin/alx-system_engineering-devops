#!/usr/bin/env ruby
# Regex using caret, dollar sign, grouping & repetition
puts ARGV[0].scan(/(^\d{10}$)/).join
