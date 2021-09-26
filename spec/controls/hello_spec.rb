

title "sample section"

# you can also use plain tests
#describe file("/tmp") do
#  it { should be_directory }
# end

# you add controls here
control "tmp-1.0" do                        # A unique ID for this control
  impact 0.7                                # The criticality, if this control fails.
  title "Hello World"                                 # Readable by a human
  desc "Text should include the words 'hello world'." # Optional description
  describe file('hello.txt') do                       # The actual test
   its('content') { should match 'test' }      # You could just do the "describe file" block if you want. The  
  end
end


describe yaml('./.github/spec/controls/test.yaml') do
  its('name') { should eq 'foo' }
  its(['array', 1]) { should eq 'one' }
end
