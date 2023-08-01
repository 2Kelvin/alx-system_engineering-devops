#!/usr/bin/env ruby
# Regex using caret, grouping & repetition
puts ARGV[0].scan(/(^\d{10,10})/).join
