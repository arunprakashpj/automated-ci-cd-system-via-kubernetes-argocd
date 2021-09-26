
title "config evaluation section"

describe yaml('kubernetes\deploy.yaml') do
  its('kind') { should eq 'Deployment' }
  its('apiVersion') { should eq 'apps/v1' }
end

describe yaml('kubernetes\service.yaml') do
  its('kind') { should eq 'Service' }
  its('apiVersion') { should eq 'v1' }
end
