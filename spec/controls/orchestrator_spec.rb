
title "config evaluation section"

describe yaml('F:\Repositories\AutomateForGood\kubernetes\deploy.yaml') do
  its('kind') { should eq 'Deployment' }
  its('apiVersion') { should eq 'apps/v1' }
end

describe yaml('F:\Repositories\AutomateForGood\kubernetes\service.yaml') do
  its('kind') { should eq 'Service' }
  its('apiVersion') { should eq 'v1' }
end