class CreateBazaarrepos < ActiveRecord::Migration
  def self.up
    create_table :bazaarrepos do |t|
      t.column :lab_id, :string
      t.column :reponame, :string
      t.column :description, :string
      t.column :created_on, :timestamp
    end
  end

  def self.down
    drop_table :bazaarrepos
  end
end
