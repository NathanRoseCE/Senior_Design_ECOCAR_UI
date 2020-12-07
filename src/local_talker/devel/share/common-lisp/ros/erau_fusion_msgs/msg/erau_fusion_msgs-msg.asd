
(cl:in-package :asdf)

(defsystem "erau_fusion_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CanBus" :depends-on ("_package_CanBus"))
    (:file "_package_CanBus" :depends-on ("_package"))
    (:file "Tracked_Lane" :depends-on ("_package_Tracked_Lane"))
    (:file "_package_Tracked_Lane" :depends-on ("_package"))
    (:file "Tracked_Lane_Object" :depends-on ("_package_Tracked_Lane_Object"))
    (:file "_package_Tracked_Lane_Object" :depends-on ("_package"))
    (:file "tracked_veh_object" :depends-on ("_package_tracked_veh_object"))
    (:file "_package_tracked_veh_object" :depends-on ("_package"))
    (:file "tracked_vehicles" :depends-on ("_package_tracked_vehicles"))
    (:file "_package_tracked_vehicles" :depends-on ("_package"))
    (:file "unfused_vehicles" :depends-on ("_package_unfused_vehicles"))
    (:file "_package_unfused_vehicles" :depends-on ("_package"))
    (:file "veh_object" :depends-on ("_package_veh_object"))
    (:file "_package_veh_object" :depends-on ("_package"))
  ))