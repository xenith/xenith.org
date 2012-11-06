Vagrant::Config.run do |config|
    config.vm.box = "xenith-org"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    config.vm.host_name = "dev.xenith.org"

    config.vm.forward_port 8000, 8000

    # Increase vagrant's patience during hang-y CentOS bootup
    # see: https://github.com/jedi4ever/veewee/issues/14
    config.ssh.max_tries = 50
    config.ssh.timeout   = 300

    config.vm.share_folder("v-root", "/srv/www/xenith.org", ".", :nfs => true)

    # Add to /etc/hosts: 33.33.33.21 dev.xenith.org
    config.vm.network :hostonly, "33.33.33.21"

    #config.vm.provision :puppet do |puppet|
    #    puppet.manifests_path = "puppet/manifests"
    #    puppet.manifest_file  = "vagrant.pp"
    #end
end
